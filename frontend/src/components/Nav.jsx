import UnderScoreSpring from "./Cursor"
import { Link } from "react-router-dom"
function Nav() {
    return (
        <nav className="navbar bg-base-100 opacity-75">
            <div className="navbar-start">

                <div className="flex-1">
                    <Link className="btn btn-ghost text-xl font-body" to="/">
                        Keeb Quiz
                        <UnderScoreSpring></UnderScoreSpring>

                    </Link>
                </div>
            </div>

            <div className="navbar-center ">
                <ul
                    tabindex="0"
                    class="menu menu-horizontal">
                    <li className="px-4"><Link to="/">Home</Link></li>
                    <li><Link to="/quizzes">Quizzes</Link></li>
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