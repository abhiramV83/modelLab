import "./Home.css";
import { useNavigate } from "react-router-dom";


function Home() {
    const navigate = useNavigate();
  return (
    <main className="home">
        <div className="home-container">
      <section className="intro">
        <h1>Train Machine Learning Models Easily</h1>
        <p>
          A simple web-based platform to upload datasets, train machine learning
          models, and understand results without writing code.
        </p>

        <button className="cta-btn" onClick={()=>navigate('/train')}>
          Get Started with Training
        </button>
      </section>


      <section className="models">
        <h2>Available Models</h2>

        <div className="model-grid">
          <div className="model-card">Linear Regression</div>
          <div className="model-card">Logistic Regression</div>
          <div className="model-card">KNN</div>
          <div className="model-card">Naive Bayes</div>
          <div className="model-card">K-Means</div>
        </div>
      </section>


      <section className="aesthetic">
        <p>
          Built for learning, experimentation, and understanding machine
          learning models through hands-on interaction.
        </p>
      </section>
      </div>
    </main>
  );
}

export default Home;
