import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then(([userResponse, photoResponse]) => ([{ status: userResponse.status, value: userResponse.value },
      { status: photoResponse.status, value: photoResponse.value }]))
    .catch(() => {
      console.log('Signup system offline');
    });
}
