import styled from 'styled-components'

const RegisterWrapper = styled.section`
  display: grid;
  align-items: center;

  .full-register-page {
    min-height: 100vh;
  }

  .logo-register {
    display: block;
    max-width: 120px;
    margin: 20px auto 140px;
  }

  .form-register {
    width: 90vw;
    max-width: 450px;
    border-top: 5px solid var(--primary-500);
    background: var(--white);
    border-radius: var(--borderRadius);
    box-shadow: var(--shadow-2);
    padding-inline: 40px;
    padding-bottom: 35px;
    margin: 0 auto;
    transition: var(--transition);
  }

  .form-row {
    margin-bottom: 0;
  }

  .form-label {
    display: block;
    font-size: var(--smallText);
    margin-bottom: 7px;
    text-transform: capitalize;
    letter-spacing: var(--letterSpacing);
  }

  .form-input {
    width: 100%;
    padding: 12px 10px;
    border-radius: var(--borderRadius);
    background: var(--backgroundColor);
    border: 1px solid var(--grey-200);
    margin-bottom: 15px;
  }

  .btn-register,
  input[type="submit"] {
    width: 100%;
    cursor: pointer;
    border-radius: 5px;
    text-decoration: none;
    margin-top: 20px;
    padding: 12px;
    font-size: 12px;
    line-height: 19px;
    text-transform: uppercase;
    font-family: "Montserrat", sans-serif;
    font-weight: 400;
    letter-spacing: 3px;
    -webkit-transition: all 0.4s ease-in-out;
    -moz-transition: all 0.4s ease-in-out;
    -ms-transition: all 0.4s ease-in-out;
    -o-transition: all 0.4s ease-in-out;
    transition: all 0.4s ease-in-out;
  }

  .btn-register {
    border: solid 2px #fff;
    background-color: black;
    color: #fff !important;
  }

  .btn-register:hover {
    border: solid 2px #fff;
    transition: opacity 0.2s;
    opacity: 0.7;
    color: white !important;
  }

  .btn-register:hover {
    color: #fff;
  }

  .btn-choose-register {
    background: transparent;
    border: transparent;
    color: #1d4ed8;
    cursor: pointer;
    letter-spacing: var(--letterSpacing);
    font-family: ALSArtemiusSans, Helvetica, sans-serif;
    font-size: 15px;
    font-weight: 400;
  }

  h5 {
    margin-bottom: 0;
    text-align: center;
    font-weight: 320;
    font-size: 30px;
  }

  p {
    margin: 1rem 0 0;
    text-align: center;
    font-family: Helvetica, sans-serif;
  }

  @media (max-width: 389px) {
    .logo-register {
      margin: 20px auto 30px;
    }
  }
`
export default RegisterWrapper
