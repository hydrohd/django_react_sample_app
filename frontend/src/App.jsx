import { useState } from 'react'

import './App.css'
import Nav from './components/Nav.jsx'
import Footer from './components/Footer.jsx'

function App() {
    return (
        <>
            <header className='fixed top-0 w-full backdrop-blur-sm border-t-2 border-primary'>
                <Nav />
            </header>

            <main>
                <div
                    className="hero min-h-screen"
                    style={{
                        backgroundImage: "url(https://i.imgur.com/lDb3gOZ.jpeg)",
                    }}>

                    <div className="hero-overlay bg-opacity-60"></div>
                    <div className="hero-content text-neutral-content text-center">
                        <div className="max-w-md">
                            <h1 className="mb-5 text-5xl font-bold font-body">Hello there</h1>
                            <p className="mb-5 font-body">
                                Provident cupiditate voluptatem et in. Quaerat fugiat ut assumenda excepturi exercitationem
                                quasi. In deleniti eaque aut repudiandae et a id nisi.
                            </p>
                            <button className="btn btn-outline btn-primary font-body">Get Started</button>
                        </div>
                    </div>

                </div>
            </main>
                
            <Footer></Footer>
        </>
    )
}

export default App
