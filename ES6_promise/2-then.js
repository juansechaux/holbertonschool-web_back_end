export default function handleResponseFromAPI(promise) {
  return promise
    .then(() => {
      console.log('Got a response from the API');
      // Return an object for resolved promise
      return {
        status: 200,
        body: 'success',
      };
    })
    .catch((error) => {
      console.error('Error:', error.message);
      // Return an empty Error object for rejected promise
      return new Error();
    });
}
