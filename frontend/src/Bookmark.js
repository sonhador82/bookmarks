import React from "react";
import { Formik, Field, Form, FieldArray } from 'formik';
import axios from "axios";

const BookmarkForm = () => (
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
              await new Promise((r) => setTimeout(r, 500));
              console.log(values)
              axios.post('http://localhost:8080/bookmark', values)
                .then( (response) => { console.log(response) })
                .catch( (error) => { console.log(error)} )
  //            alert(JSON.stringify(values, null, 2));
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
        </div>
)

export default BookmarkForm
