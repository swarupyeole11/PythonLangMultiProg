// way to call a get rquest using asnync await
 async function logMovies() {
    const response = await fetch("https://jsonplaceholder.typicode.com/posts");
    const movies = await response.json();
    return movies
  }

 logMovies().then((data) => console.log(data))





// respo = fetch('https://jsonplaceholder.typicode.com/posts', {
//   method: 'POST',
//   body: JSON.stringify({
//     title: 'foo',
//     body: 'bar',
//     userId: 1,
//   }),
//   headers: {
//     'Content-type': 'application/json; charset=UTF-8',
//   },
// })
//   .then((response) => response.json()).then((json)=> json)

// console.log(respo)