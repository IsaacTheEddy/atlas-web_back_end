import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, filename) {
  const signUp = await signUpUser(firstName, lastName).then((results) => ({
    status: 'fulfilled',
    value: results,
  }));

  const upload = await uploadPhoto(filename).catch((err) => ({
    status: 'rejected',
    value: err.toString(),
  }));

  return Promise.resolve([signUp, upload]);
}
