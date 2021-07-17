//const BASE_URL = '.';

function upload(formData) {
    const url = `/api/audio/upload`;

    return fetch(url, {
        method: 'post',
        body: formData,
    })
    .then((x) => x.json());
}

export { upload }