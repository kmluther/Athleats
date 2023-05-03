import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import { useFormik } from 'formik';
import { Col, Container } from 'react-bootstrap';
import * as yup from 'yup';
import './Authentication.css'

function Authentication({ updateUser }) {
    const [signUp, setSignUp] = useState(false);
    const history = useHistory();

    const handleClick = () => setSignUp((signUp) => !signUp);

    const formSchema = yup.object().shape({
        username: yup.string.required('Please enter your first name'),
        email: yup.string().email().required('Please enter your email'),
        password: yup.string().required('Please enter a password'),
        age: yup.integer().required('Please enter your age'),
        weight: yup.integer().required('Please enter your weight in pounds'),
        primary_sport: yup.string('Please enter your primary sport')
    });

    const formik = useFormik({
        initialValues: {
            username: '',
            age: '',
            weight: '',
            primary_sport: '',
            email: 'example@gmail.com',
            password: 'password',
        },
        validationSchema: formSchema,
        onSubmit: (values) => {
            console.log(values)
            fetch(signUp ? '/signup' : '/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ ...values, password: values.password }, null, 2),
            }).then((resp) => {
                if (resp.ok) {
                    resp.json().then((user) => {
                        updateUser(user);
                    });
                } else {
                resp.json().then(console.log);
                }
            });
        },
    });

    return (
        <div className="Authentication">
            <Container fluid className='p-0'>
                <VideoContainer />
                <Col className='left-col vh-100 d-flex flex-column position-absolute justify-content-center end-0 top-0 p-5'>
                    <form>
                        <h3>{signUp ? 'Sign up now!' : 'Please sign in'}</h3>
                        {signUp && formik.errors && (
                            <>
                                <label htmlFor='username'>Username:</label>
                                <input
                                    type='text'
                                    id='username'
                                    name='username'
                                    onChange={formik.handleChange}
                                    value={formik.values.username}
                                />
                                <label>Primary Sport:</label>
                                <label className='mt-0'>
                                    <input
                                        type='radio'
                                        id='run'
                                        name='type'
                                        value='Run'
                                        onChange={formik.handleChange}
                                        checked={formik.values.type === 'Run'}
                                    />
                                    Run
                                </label>
                                <label className='mt-0'>
                                    <input
                                        type='radio'
                                        id='bike'
                                        name='type'
                                        value='Bike'
                                        onChange={formik.handleChange}
                                        checked={formik.values.type === 'Bike'}
                                    />
                                    Bike
                                </label>
                                <span>{formik.errors.type}</span>
                            </>
                        )}
                        <label htmlFor='email'>Email</label>
                        <input
                            type='text'
                            id='email'
                            name='email'
                            onChange={formik.handleChange}
                            value={formik.values.email}
                        />
                        <span>{formik.errors.email}</span>
                        <label htmlFor='password'>Password</label>
                        <input
                            type='password'
                            id='password'
                            name='password'
                            onChange={formik.handleChange}
                            value={formik.values.password}
                        />
                        <span>{formik.errors.password}</span>
                        <button type='submit' onClick={formik.handleSubmit}>
                            {signUp ? 'Sign up now!' : 'Sign in'}
                        </button>
                    </form>

                    <h6 className='mt-3'>{signUp ? 'Already a member?' : 'Not a member?'}</h6>

                    <a href='#' onClick={handleClick}>{signUp ? 'Log In!' : 'Sign Up!'}</a>
                </Col>
            </Container>
        </div>
    );
}

export default Authentication