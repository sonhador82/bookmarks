import React, { useState } from "react";
import { Formik, Field, Form, FieldArray } from 'formik'
import { Form as BootstrapForm } from "react-bootstrap";
import axios from "axios";
import BACKEND_URL from "../../Config";

const AddBookmark = () => {
    const [status, setStatus] = useState("test")
    return (
          <div>
            <h1>Sign Up</h1>
            <Formik
              initialValues={{
                url: '',
                title: '',
                description: '',
                category: '',
                tags: ''
              }}
              onSubmit={async (values) => {
                console.log(values)
                axios.post(`${BACKEND_URL}/bookmark`, values)
                  .then( (response) => { setStatus(response.statusText) })
                  .catch( (error) => { setStatus(error.toString())} )
                }}
            >
              <Form>
                <BootstrapForm.Group className="mb-3" controlId="url">
                  <BootstrapForm.Label>Url</BootstrapForm.Label>
                  <Field id="url" name="url" placeholder="Url" />
                </BootstrapForm.Group>

                <BootstrapForm.Group className="mb-3" controlId="label">
                  <label htmlFor="title">Title</label>
                  <Field id="title" name="title" placeholder="Title" />
                </BootstrapForm.Group>

                <BootstrapForm.Group className="mb-3" controlId="description">
                  <label htmlFor="description">Description</label>
                  <Field id="description" name="description" placeholder="Description" />
                </BootstrapForm.Group>
                
                <BootstrapForm.Group className="mb-3" controlId="label">
                  <label htmlFor="category">Category</label>
                  <Field id="category" name="category" placeholder="Category" />
                </BootstrapForm.Group>

                <BootstrapForm.Group className="mb-3" controlId="label">
                  <label htmlFor="tags">Tags (w comma)</label>
                  <Field id="tags" name="tags" placeholder="tags" />
                </BootstrapForm.Group>

                <button type="submit">Submit</button>
              </Form>
            </Formik>
            <div>Status: {status}</div>
          </div>
          
    )
  }

export default AddBookmark
