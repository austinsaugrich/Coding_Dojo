import './App.css'
import Header from './componets/Header';
import Nav from './componets/Navigation';
import MainContent from './componets/MainContent';



function App() {
    return (
      <>
        <div className='appcontainer'>
          <Header/>
          <div className='container'>
            <Nav/>
            <MainContent/>
          </div>
        </div>
      </>
    );
  }
  
export default App



