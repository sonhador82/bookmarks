


const ShowBookmarks = () => {

    const getBookmarks = () => {
        return [
            {
                "url": "https://ya.ru",
                "title": "yandex",
                "description": "someText"
            }
        ]
    }

    const listBookmarks = getBookmarks().map((bookmark) => 
        <li>{bookmark.title}</li>
    )

    return (
        <div>
            {listBookmarks}
        </div>

    )
}

export default ShowBookmarks