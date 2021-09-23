import React, { useState } from "react";
import { Formik, Field, Form, FieldArray } from 'formik';
import axios from "axios";

function BookmarkForm() {
  const [status, setStatus] = useState("test")

  return (
        <div>
          <h1>Sign Up</h1>
          <Formik
            initialValues={{
              url: '',
              title: '',
              category: '',
              tags: ''
            }}
            onSubmit={async (values) => {
              console.log(values)
              axios.post('http://localhost:8080/bookmark', values)
                .then( (response) => { setStatus(response.statusText) })
                .catch( (error) => { setStatus(error.toString())} )
              }}
          >
            <Form>
              <label htmlFor="url">Url</label>
              <Field id="url" name="url" placeholder="Url" />
      
              <label htmlFor="title">Title</label>
              <Field id="title" name="title" placeholder="Title" />
      
              <label htmlFor="category">Category</label>
              <Field id="category" name="category" placeholder="Category" />

              <label htmlFor="tags">Category</label>
              <Field id="tags" name="tags" placeholder="tags" />

              <button type="submit">Submit</button>
            </Form>
          </Formik>
          <div>Status: {status}</div>
        </div>
        
  )
}

export default BookmarkForm
