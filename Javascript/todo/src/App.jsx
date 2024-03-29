import Form from './components/add'
import Task from './components/delete'
import './App.css'
import { useState } from 'react'

function App(){
  const [currentTask, setCurrentTasks] = useState([])

  const onNewTask = (newTask) => {
    setCurrentTasks([...currentTask,newTask]);
  }

  const onDeleteTask = (index) => {
    setCurrentTasks(currentTask.filter((task, taskIndex) => {return taskIndex !== index}));
    
  }


  const handleToggleComplete = (index) => {
    const updatedTasks = [...currentTask];
    updatedTasks[index] = updatedTasks[index].startsWith('✓') ? updatedTasks[index].substring(2) : '✓ ' + updatedTasks[index];
    setCurrentTasks(updatedTasks);
  };

  return (
    <div>
      <Form onNewTask={onNewTask}/>
      <Task currentTask={currentTask} onDeleteTask={onDeleteTask} onToggleComplete={handleToggleComplete}/>
    </div>
  )
}




export default App
