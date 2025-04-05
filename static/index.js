function buttonfunc(){
  fetch("http://127.0.0.1:5000/buttoncatcher", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({input: "hello"})
  })
}
