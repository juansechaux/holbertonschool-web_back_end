export default function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    // successful response
    resolve('apiResponse');
    // If there was an error, the Promise is rejected with an error.
    reject(new Error('Error fetching data from API'));
  });
}
