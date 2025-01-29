export default function signUpUser(firstName, lastName) {
  const names = new Promise((resolve) => {
    resolve(
      { firstName, lastName },
    );
  });
  return names;
}
