function Home() {
    return (
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
    )
}

export default Home