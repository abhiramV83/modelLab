import { useState } from 'react'
import './MainApp.css'

function MainApp() {
const [modelName,setModel] = useState("")
const [file,setFile] = useState(null)
const [ans,setAns] = useState({
  model_name: "No model yet",
  result_is: "—"
})
const handleSubmit =async ()=> {
      if (!file || modelName === "" || modelName === "Select_option") {
      alert("Please select a model and upload a CSV file");
      return;
    }
      const formdata = new FormData();
      formdata.append('file',file);
      formdata.append('model',modelName);
      const res = await fetch("http://localhost:8000/train",{
        method:"POST",
        body:formdata,
      }
      )
      const result = await res.json();
        console.log(result);  
        setAns(result)  
}
  
  
  return (
    <div className="page">
      <div className="home-container">
      <div className="top-section">
        <div className="inputs-card">
          <h2>Train Model</h2>

          <select onChange={(e) => setModel(e.target.value)}>
            <option value="Select_option">Select option</option>
            <option value="Naive_Bayes">Naive Bayes</option>
            <option value="K_Nearest_Neighbours">KNN</option>
            <option value="Linear_Regression">Linear Regression</option>
            <option value="Logistic_Regression">Logistic Regression</option>
          </select>

          <input
            type="file"
            accept=".csv"
            onChange={(e) => setFile(e.target.files[0])}
          />

          <button onClick={handleSubmit}>Train Model</button>
        </div>

        <div className="notes-card">
          <h2>Model Notes</h2>
          
          <button className="read-more">Read more</button>
        </div>

      </div>

      {/* BOTTOM – OUTPUT */}
      <div className="output-card">
        <h2>Output</h2>
        <p><strong>Model:</strong> {ans.model_name}</p>
        <p><strong>Result:</strong> {ans.result_is}</p>
      </div>
    </div>
    </div>
  )
  

}

export default MainApp
