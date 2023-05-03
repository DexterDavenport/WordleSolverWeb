async function handleSubmit(event) {
  event.preventDefault();

  const formData = new FormData(event.target);
  const data = Object.fromEntries(formData.entries());

  for (const key in data) {
    if (data[key] === '') {
      data[key] = null;
    }
  }

  console.log('Form data:', data);

  const response = await fetch('/search', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  });

  const results = await response.json();

  console.log('Results:', results);

  displayResults(results);
}

function clearForm() {
  document.getElementById("search-form").reset();
  document.getElementById("results").innerHTML = "";
}

function displayResults(words) {
  const resultsContainer = document.getElementById("results");
  resultsContainer.innerHTML = "";
  const wordsPerColumn = 20;

  if (words.length === 0) {
    const noResults = document.createElement("p");
    noResults.textContent = "No results found.";
    resultsContainer.appendChild(noResults);
  } else {
    const columns = Math.ceil(words.length / wordsPerColumn);
    const grid = document.createElement("div");
    grid.style.display = "grid";
    grid.style.gridTemplateColumns = `repeat(${columns}, 1fr)`;
    grid.style.gap = "1rem";
    resultsContainer.appendChild(grid);

    for (let i = 0; i < columns; i++) {
      const list = document.createElement("ul");
      const startIndex = i * wordsPerColumn;
      const endIndex = Math.min(startIndex + wordsPerColumn, words.length);

      for (let j = startIndex; j < endIndex; j++) {
        const listItem = document.createElement("li");
        listItem.textContent = words[j];
        list.appendChild(listItem);
      }

      grid.appendChild(list);
    }
  }
}

function main() {
  document.getElementById("search-form").addEventListener("submit", handleSubmit);
  document.getElementById("clear-button").addEventListener("click", clearForm);
}

document.addEventListener("DOMContentLoaded", main);
