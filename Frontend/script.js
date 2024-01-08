function fetchData1() {
    fetch('http://127.0.0.1:5000/item')
        .then(response => response.json())
        .then(data => {
            displayData(data);
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('resultContainer').innerHTML = 'Error fetching data.';
        });
}

function fetchData2() {
    fetch('http://127.0.0.1:5000/store')
        .then(response => response.json())
        .then(data => {
            displayData(data);
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('resultContainer').innerHTML = 'Error fetching data.';
        });
}

function deleteStore() {
    const storeId = document.getElementById('deleteInput').value;

    fetch(`http://127.0.0.1:5000/store/${storeId}`, {
        method: 'DELETE',
    })
        .then(response => response.json())
        .then(data => {
            console.log(data); // Log the response from the server after deletion
            fetchData2(); // Fetch and display updated store data after deletion
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('resultContainer').innerHTML = 'Error deleting store.';
        });
}

function displayData(data) {
    const resultContainer = document.getElementById('resultContainer');
    resultContainer.innerHTML = ''; // Clear previous content

    const jsonList = document.createElement('ul');
    jsonList.classList.add('json-list');

    for (const key in data) {
        const listItem = document.createElement('li');
        listItem.classList.add('json-item');

        const keyElement = document.createElement('span');
        keyElement.classList.add('json-key');
        keyElement.textContent = key + ':';

        const valueElement = document.createElement('span');
        valueElement.classList.add('json-value');
        valueElement.textContent = JSON.stringify(data[key]);

        listItem.appendChild(keyElement);
        listItem.appendChild(valueElement);
        jsonList.appendChild(listItem);
    }

    resultContainer.appendChild(jsonList);
}

document.getElementById('fetchDataButton1').addEventListener('click', fetchData1);
document.getElementById('fetchDataButton2').addEventListener('click', fetchData2);
document.getElementById('delete').addEventListener('click', deleteStore);




















// fetch('http://127.0.0.1:5000/store')
// .then((response)=>{
//     return response.json()
// })
// .then((data)=>{
//     console.log(data);
// })
// .catch((error) => console.log('E : ', error)
// )



// function fetchData() {
//     fetch('http://127.0.0.1:5000/item')
//     // fetch('http://127.0.0.1:5000/store')
//         .then(response => {
            
//             return response.json();
//         })
//         .then(data => {
//             // Display the data on the webpage
//             document.getElementById('resultContainer').innerHTML = JSON.stringify(data, null, 2);


//             // console.log(data);
//         })
//         .catch(error => {
//             console.error('Error:', error);
//             document.getElementById('resultContainer').innerHTML = 'Error fetching data.';
//         });
// }

// document.getElementById('fetchDataButton').addEventListener('click', fetchData);





