const submit_btn = document.querySelector(".submit_btn");
const feild_text = document.querySelector(".feild_text");

async function getData(url) {
  const response = await fetch(url);
  console.log(response);
  const data = response.json();
  // console.log(data)

  return data;
}

submit_btn.addEventListener("click", async () => {
  // feild_input = submit_btn.value;

  // feild_text.innerHTML = feild_input;

  let result = await getData("/getdata");
  console.log(result);
  feild_text.innerHTML = result;
});

// fetch("")
//  addEventListener("click", () => {

// } )
