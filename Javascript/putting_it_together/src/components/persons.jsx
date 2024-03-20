import { useState } from 'react';



const Persons = (props) =>{
    const {lastName, firstName, age, hairColor} = props;
    const [personAge, setAge] = useState(age)
    return(
        <>
        <div className="appcontainer">
            <div className="container">
                <h1>{lastName}, {firstName}</h1>
                <div className="rows">
                    <p>Age:</p>
                    <p>{personAge}</p>
                </div>
                <div className="rows">
                    <p>Hair Color:</p>
                    <p>{hairColor}</p>
                </div>
            </div>
        </div>
        <div className="button">
                    <button onClick={ () => setAge(personAge + 1)}>Birthday Button for {firstName} {lastName}</button>
            </div>
        </>

    )
}

export default Persons;