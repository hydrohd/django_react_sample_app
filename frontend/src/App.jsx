import { useState } from 'react'

import './App.css'
import Nav from './components/Nav.jsx'
import Footer from './components/Footer.jsx'
import Home from './pages/Home.jsx'
import Quizzes from './pages/Quizzes.jsx'
import { Route, Routes } from 'react-router-dom'
function App() {
    return (
        <>
            <header className='fixed top-0 w-full backdrop-blur-sm border-t-2 border-primary'>
                <Nav />
            </header>
            
            <main>
                <Routes>
                    <Route path='/' element={<Home />} />
                    <Route path='/quizzes' element={<Quizzes />} />
                </Routes>
            </main>
                
            <Footer></Footer>
        </>
    )
}

export default App
