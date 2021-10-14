import { Container, Form, Col, Row, Button } from "react-bootstrap"

const AddBookmark = () => {
    return (
        <Container>
            <Form>
                <Row className="mb-3">
                    <Col xs={7}>
                        <Form.Group controlId="formTitle">
                            <Form.Label>Title</Form.Label>
                            <Form.Control type="text" placeholder="Title" />
                        </Form.Group>
                    </Col>

                    <Form.Group as={Col} controlId="formLabels">
                        <Form.Label>Labels</Form.Label>
                        <Form.Control type="text" placeholder="devops,ci/cd,databases" />
                    </Form.Group>
                </Row>

                <Row>
                    <Col xs={7}>
                        <Form.Group className="mb-3" controlId="formUrl">
                            <Form.Label>Url</Form.Label>
                            <Form.Control type="text" placeholder="https://somsite.com/nice-article" />
                        </Form.Group>
                    </Col>
                        <Form.Group as={Col} controlId="formCategory">
                            <Form.Label>Category</Form.Label>
                            <Form.Control type="text" placeholder="somecat" />
                        </Form.Group>

                </Row>

                <Form.Group className="mb-3" controlId="formDescription">
                    <Form.Label>Description</Form.Label>
                    <Form.Control as="textarea" placeholder="Some description" style={{ height: '100px' }} />
                </Form.Group>

                <Button variant="primary" type="submit">Submit</Button>
            </Form>

        </Container>
    )
}

export default AddBookmark
