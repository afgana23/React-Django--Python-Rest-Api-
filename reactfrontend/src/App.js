
import './App.css';
import {useState,useEffect} from "react";
import axios from "axios";

function App() {
 const[stdn,setStdn]=useState([])
 useEffect(()=>{
  async function getAllStudent(){

    try{
      const customers= await axios.get("http://127.0.0.1:8000/showgenapi/")
      console.log(customers.data)
      setStdn(customers.data)

    } catch(error){

    }
  }
  getAllStudent()
 } ,[]) 

  return (
    <div className="App">
      <header className="App-header">
        <h1>Connect React to Django</h1>
        { 
              
            stdn.map((st,i)=>{
            return(
              <table border={2}>
              <tr>
                <th>name</th>
                <th>age</th>
                <th>phone</th>
                <th>address</th>
              </tr>
             
                <tr>
                  <td key={i}>
                    {st.c_name}
                    
                  </td>
                  <td>{st.age}</td>
                  <td>{st.phone}</td>
                  <td>{st.address}</td>
                </tr>

              </table>
             
            )
          })
        }
      </header>
    </div>
  );
}

export default App;
