import { useEffect, useState } from "react"
import axios from "axios"
import { rest } from "lodash"
import { Card, Button, Container, Row, Table } from "react-bootstrap"
import BACKEND_URL from "../../Config"


const ShowBookmarks = () => {
    const [bookmarks, setBookmarks] = useState([]);
    const fetchBookmarks = async () => {
        try {
            const resp = await axios.get(`${BACKEND_URL}/api/bookmarks`, { withCredentials: true })
            if (resp.status === 200) {
                setBookmarks(resp.data)
            }            
        } catch (error) {
            console.log(error)
        }
    }

    useEffect(() => {
        fetchBookmarks()
    }, [])

    return (
        <Container>
            <Table size="sm">
                <tbody>
                    {bookmarks.map(function (item, idx) {
                        return (
                            <tr key={idx}>
                                <td>{item.title}</td>
                                <td><a target="_blank" href={item.url}>{item.url}</a></td>
                                <td>{item.user_id}</td>
                                <td>{item.category}</td>
                            </tr>
                        )
                    })}
                </tbody>
            </Table>
        </Container>

    )
}

export default ShowBookmarks