#!/usr/bin/env python3
"""This module filters through a password with
Regex"""
import re
from typing import List
import logging
import mysql
from mysql.connector import connect, MySQLConnection
import os
import datetime

import mysql.connector

host_name = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
user_name = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
user_pass = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
db_name = os.getenv('PERSONAL_DATA_DB_NAME', 'my_db')


PII_FIELDS = ("name", "email", "ssn", "password", "phone")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """COnstructor class"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Formats the log message with redactions"""
        log_message = super().format(record)

        return filter_datum(self.fields, self.REDACTION, log_message,
                            self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Splits and replaces a string using regex"""
    pattern = rf'({("|".join(fields))})=([^;]*?)(?={separator}|$)'
    return re.sub(pattern, lambda match:
                  f"{match.group(1)}={redaction}", message)


def get_logger() -> logging.Logger:
    """Returns a logging object"""
    log = logging.getLogger("user_data")

    log.setLevel(logging.INFO)

    log.propagate = False

    handler = logging.StreamHandler()

    format = RedactingFormatter(fields=PII_FIELDS)
    handler.setFormatter(format)

    log.addHandler(handler)

    return log


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Conncects to a mysql database"""
    connection = connect(
        host=host_name,
        user=user_name,
        password=user_pass,
        database=db_name
        )
    return connection


def main() -> None:
    """Main function"""
    db = get_db()

    pii = {
        "name": "name",
        "email": "email",
        "phone": "phone",
        "ssn": "ssn",
        "password": "password"
        }

    cursor = db.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    for user in users:
        data = {
            "name": user[0],
            "email": user[1],
            "phone": user[2],
            "ssn": user[3],
            "password": user[4],
            "ip": user[5],
            "last_login": user[6],
            "user_agent": user[7]
            }

        user_str = '; '.join(f"{key}={value}" for key, value in data.items())

        # Redact sensitive information
        filtered_user = filter_datum(pii.keys(), "***", user_str, ";")
        print(f"[HOLBERTON] user_data INFO {datetime.datetime.now()}\
              :{filtered_user}")
        if cursor:
            cursor.close()

        # Ensure the database connection is closed
        if db:
            db.close()


if __name__ == "__main__":
    main()
