import {useSpring, animated} from 'react-spring'

const UnderScoreSpring = () => {
    const styles = useSpring({
        loop: { reverse: true },
        from: { opacity: 1 },
        to: { opacity: 0 },
        delay: 100,
    })

    return (
        <animated.div style={styles}>     
            &#9612;
        </animated.div>

    )
}

export default UnderScoreSpring