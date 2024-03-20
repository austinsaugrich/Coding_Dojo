import Persons from './components/persons'
import './App.css'

function App(){
  return (
    <>
    <div className='rootcontainer'>
      <Persons firstName="Jane" lastName="Doe" age={45} hairColor="Black" />
      <Persons firstName="John" lastName="Smith" age={88} hairColor="Brown"/>
    </div>
    </>
  )
}

export default App
