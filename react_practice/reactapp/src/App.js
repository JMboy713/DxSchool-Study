import './App.css';
import MyComponent from './MyComponent';
import Sample from './Sample';
import EventComponent from './EventComponent';


function App() {
  
  return (
    <>
    <EventComponent/>
    <MyComponent team='doosan'/> 
    <Sample team='SSG'> 2등 </Sample>
    </>
  );
}                                                                                                                                                                       

export default App;
