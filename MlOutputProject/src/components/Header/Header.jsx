import { NavLink } from "react-router-dom";
import "./Header.css";
function Header() {
  return (
    <header className='header'>
        <div className="app-container header-inner">
          <div>
        <NavLink to='/' className='active-logo'>
        ModelLab
        </NavLink>
        </div>
        <nav className="nav">
            <NavLink to="/" className={({isActive})=> isActive?'active':'not-active'}>
            Home
            </NavLink>
            <NavLink to="https://abhiramv83.github.io/portfolio/" className={({isActive})=> isActive?'active':'not-active'} >Developer</NavLink>
        </nav>
        </div>
    </header>
  )
}

export default Header