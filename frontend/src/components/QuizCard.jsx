import keeb from './../assets/images/keeb.jpeg'

function QuizCard() {

    return (
        <div class="flex items-center justify-center p-4">
            <div className="card bg-base-100 image-full w-96 shadow-xl">
                <figure>
                    <img
                        src={keeb}
                        alt="Shoes" />
                </figure>
                <div className="card-body">
                    <h2 className="card-title">Shoes!</h2>
                    <p>If a dog chews shoes whose shoes does he choose?</p>
                    <div className="card-actions justify-end">
                        <button className="btn btn-outline btn-primary">Buy Now</button>
                    </div>
                </div>
            </div>

        </div>

    )

}

export default QuizCard