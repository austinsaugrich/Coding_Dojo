import { useState } from 'react';



const Form = () => {
    const [firstName, setfirstName] = useState("");
    const [firstNameError, setFirstNameError] = useState("");
    const [lastName, setlastName] = useState("");
    const [lastNameError, setLastNameError] = useState("");
    const [email, setEmail] = useState("");
    const [emailError, setEmailError] = useState("");
    const [password, setPassword] = useState("");
    const [passwordError, setPasswordError] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    const [confirmPasswordError, setConfirmPasswordError] = useState("");
    const [hasBeenSubmitted, setHasBeenSubmitted] = useState(false);
    


    const validatefirstName = (e) => {
        setfirstName(e.target.value);
        if(e.target.value.length < 2) {
            setFirstNameError("First name needs to be longer than 2 characters!");
        } else {
            setFirstNameError("");
        }
    }

    const validateLastName = (e) => {
        setlastName(e.target.value);
        if(e.target.value.length < 2) {
            setLastNameError("Last name needs to be longer than 2 characters!");
        } else {
            setLastNameError("");
        }
    }

    const validateEmail = (e) => {
        setEmail(e.target.value);
        if(e.target.value.length < 8) {
            setEmailError("Email needs to be longer than 8 characters!");
        } else {
            setEmailError("");
        }
    }
    const validatePassword = (e) => {
        setPassword(e.target.value);
        if(e.target.value.length < 8) {
            setPasswordError("Password needs to be longer than 8 characters!");
        } else {
            setPasswordError("");
        }
    }
    const validateConfirmPassword = (e) => {
        setConfirmPassword(e.target.value);
        if(e.target.value !== password ) {
            setConfirmPasswordError("Passwords need to match!");
        } else {
            setConfirmPasswordError("");
        }
    }

    const createUser = (e) => {
        e.preventDefault();
        
        const newUser = { firstName, email, password, lastName, confirmPassword };
        console.log("Welcome", newUser);
            setfirstName("");
            setlastName("");
            setEmail("");
            setPassword("");
            setConfirmPassword("");
    
        setHasBeenSubmitted( true );
    };
    
    
    return (
        <div className='appcontainer'>
        <form onSubmit={ createUser }>
            {
            hasBeenSubmitted ? 
            <h3>Thank you for submitting the form!</h3> :
            <h3>Welcome, please submit the form.</h3> 
    }
            <div className='rows'>
                <label>First Name: </label> 
                <input type="text" value={firstName} onChange={ validatefirstName } />
                {
                    firstNameError ?
                    <p>{ firstNameError }</p>:
                    ""
                }
            </div>
            <div className='rows'>
                <label>Last Name: </label> 
                <input type="text" value={lastName} onChange={ validateLastName } />
                {
                    lastNameError ?
                    <p>{ lastNameError }</p>:
                    ""
                }
            </div>
            <div className='rows'>
                <label>Email Address: </label> 
                <input type="text" value={email} onChange={ validateEmail } />
                {
                    emailError ?
                    <p>{ emailError }</p>:
                    ""
                }
            </div>
            <div className='rows'>
                <label>Password: </label>
                <input type="text" value={password} onChange={ validatePassword } />
                {
                    passwordError ?
                    <p>{ passwordError }</p>:
                    ""
                }
            </div>
            <div className='rows'>
                <label>Confirm Password: </label>
                <input type="text" value={confirmPassword} onChange={ validateConfirmPassword } />
                {
                    confirmPasswordError ?
                    <div className='error'>
                    <p>{ confirmPasswordError }</p> </div>:
                    ""
                    
                }
            </div>
            <div className='button'>
            <input type="submit" value="Create User" />
            </div>
        </form>
        </div>
    );
};
    
export default Form;