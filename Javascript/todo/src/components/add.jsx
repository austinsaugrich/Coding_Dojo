import { useState } from "react";

const Form = (props) => {
    const [task, setTask] = useState("");
    



    const createTask = (e) => {
        e.preventDefault();
        props.onNewTask(task);
        setTask("");
    }

    



        return(
            <div className="add">
                <div>
                    <form onSubmit={ createTask }>
                        <label>Task to add:</label>
                        <input type="text" onChange={ (e) => setTask(e.target.value)} value={task} />
                      
                        <input type="submit" value='Add'/>
                    </form>
                </div>
            </div>
        )
    
    
}
export default Form;