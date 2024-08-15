import QuizCard from "../components/QuizCard"

function Quizzes() {

    return (
        <div className="min-h-screen">

            <div className="flex-col py-20">

                <div className="flex justify-center py-6">

                    <div className="border-2 border-secondary rounded-b-lg p-2">
                        <h1 className="text-5xl font-bold font-body">Active Quizzes</h1>
                    </div>


                </div>

                <div className="grid grid-cols-3 gap-10 mx-auto w-full">
                        <QuizCard></QuizCard>
                        <QuizCard></QuizCard>
                        <QuizCard></QuizCard>
                        <QuizCard></QuizCard>
                        <QuizCard></QuizCard>
                    </div>
            </div>
        </div>
    )

}

export default Quizzes