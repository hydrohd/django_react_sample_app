import UnderScoreSpring from "./Cursor"

function Nav() {
    return (
        <nav className="navbar bg-base-100 opacity-75">
            <div className="navbar-start">

                <div className="flex-1">
                    <a className="btn btn-ghost text-xl font-body">
                        Keeb Quiz
                        <UnderScoreSpring></UnderScoreSpring>

                    </a>
                </div>
            </div>

            <div className="navbar-center ">
                <ul
                    tabindex="0"
                    class="menu menu-horizontal">
                    <li className="px-4"><a className="active">Home</a></li>
                    <li><a>Quizzes</a></li>
                </ul>
            </div>


            <div className="navbar-end">
                <div className="flex-none">
                    <button className="btn btn-square btn-ghost">
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            className="inline-block h-5 w-5 stroke-current">
                            <path
                                strokeLinecap="round"
                                strokeLinejoin="round"
                                strokeWidth="2"
                                d="M5 12h.01M12 12h.01M19 12h.01M6 12a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0z"></path>
                        </svg>
                    </button>
                </div>

            </div>


        </nav>
    )

}




export default Nav