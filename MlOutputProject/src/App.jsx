import { createBrowserRouter, createRoutesFromElements, Route, RouterProvider } from 'react-router-dom'
import Layout from './Layout.jsx'
import MainApp from './components/Home/MainApp.jsx'
import Home from './components/Home/Home.jsx'

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path='/' element={<Layout/>}>
        <Route path=''element={<Home/>}/>
        <Route path='/train'element={<MainApp/>} />
    </Route>
  )
)
function App(){
    return <RouterProvider router={router} />
  }
export default App