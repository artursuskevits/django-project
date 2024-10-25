// URL API
const apiUrl = 'http://127.0.0.1:8000/ads/';

// Функция для получения списка объявлений
function loadAds() {
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            const adsContainer = document.getElementById('ads-container');
            adsContainer.innerHTML = ''; // Очищаем контейнер перед загрузкой

            data.forEach(ad => {
                const adElement = document.createElement('div');
                adElement.className = 'ad';

                const adContent = `
                    <h3>${ad.title}</h3>
                    <img src="${ad.photo_links[0]}" alt="Фото объявления">
                    <p>Цена: ${ad.price} руб.</p>
                `;

                adElement.innerHTML = adContent;
                adsContainer.appendChild(adElement);
            });
        })
        .catch(error => console.error('Ошибка:', error));
}

// Загружаем объявления при загрузке страницы
window.onload = loadAds;
// Обработчик отправки формы создания объявления
document.getElementById('create-ad-form').addEventListener('submit', function(e) {
    e.preventDefault();

    const title = document.getElementById('title').value;
    const description = document.getElementById('description').value;
    const price = document.getElementById('price').value;
    const photoLinks = document.getElementById('photo_links').value.split(',');

    const adData = {
        title: title,
        description: description,
        price: price,
        photo_links: photoLinks
    };

    fetch(apiUrl + 'create/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(adData)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').textContent = `Объявление создано с ID: ${data.id}`;
        loadAds();  // Перезагружаем список объявлений
    })
    .catch(error => console.error('Ошибка:', error));
});
