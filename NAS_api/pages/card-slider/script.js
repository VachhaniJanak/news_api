const card_wrapper = document.getElementById("card-wrapper");
const loading = document.getElementById("loading");
var flage = true;
var flage0 = true;

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function gettoken() {
  for (let i of document.cookie.split(";")) {
    let key = i.split("=")[0];
    if (key == "tokenid") {
      return i.split("=")[1];
    }
  }
}

async function typeWriter(txt) {
  if (flage0) {
    flage0 = false;
    document.getElementById("summary-text").innerHTML = "";
    for (let i = 0; i < txt.length; i++) {
      document.getElementById("summary-text").innerHTML += txt.charAt(i);
      await sleep(6);
    }
    flage0 = true;
  }
}

async function getsummary(id) {
  if (flage) {
    flage = false;
    loading.className = "loader";
    await fetch("http://127.0.0.1:8000/get_summary", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        token_id: gettoken(),
        article_id: id,
        count: 0,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        typeWriter(data.summary);
      });
    flage = true;
    loading.className = "";
  }
}

function create_item(data) {
  const card_item = document.createElement("div");
  const card_link = document.createElement("a");
  const card_image = document.createElement("img");
  const disc_item = document.createElement("div");
  const item_header = document.createElement("div");
  const card_title = document.createElement("h2");
  const badge_designer = document.createElement("p");
  const description = document.createElement("p");
  const card_button = document.createElement("button");

  card_item.className = "card-item";
  card_link.className = "card-link";
  card_image.className = "card-image";
  disc_item.className = "disc-item";
  item_header.className = "item-header";
  card_title.className = "card-title";
  badge_designer.className = "badge badge-designer";
  description.className = "description";
  card_button.className = "card-button material-symbols-rounded";

  //   card_link.href = data.url;
  card_image.src = data.img_src;
  card_image.alt = "Card Image";
  card_title.textContent = data.headline;
  badge_designer.textContent = data.site;
  description.textContent = data.context.slice(0, 200) + "....";
  card_button.innerHTML = "arrow_forward";
  card_button.setAttribute("onclick", `getsummary(${data.article_id})`);
  card_item.appendChild(card_link);
  card_link.appendChild(card_image);
  card_link.appendChild(disc_item);
  disc_item.appendChild(item_header);
  item_header.appendChild(card_title);
  item_header.appendChild(badge_designer);
  disc_item.appendChild(description);
  disc_item.appendChild(card_button);

  return card_item;
}

window.onload = function () {
  const resp = fetch("http://127.0.0.1:8000/get_articles", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      token_id: gettoken(),
      article_id: 1,
      count: 0,
    }),
  });

  resp
    .then((response) => response.json())
    .then((data) => {
      loaddata(data.data);
    });
};

function loaddata(data) {
  for (let i = 0; i < data.length; i++) {
    card_wrapper.appendChild(create_item(data[i]));
  }
}

function loadmore() {
  const count = document.getElementById("card-wrapper").childElementCount;
  const resp = fetch("http://127.0.0.1:8000/get_articles", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      token_id: gettoken(),
      article_id: 1,
      count: count,
    }),
  });

  resp
    .then((response) => response.json())
    .then((data) => {
      loaddata(data.data);
    });
}
