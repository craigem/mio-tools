-- Calculate Parabola results

main = do
    -- Grab the height
    number <- prompt "Please provide the height: "
    let height = read number :: Float
    -- Grab the width
    number <- prompt "Please provide the width: "
    let width = read number :: Float
    -- Calculate the Length of an Arc:
    calculateArcLength height width

calculateArcLength :: Float -> Float -> IO ()
calculateArcLength height width = do
    -- Calculate the length of the arc of the parabola:
    let arcLength =
                    sqrt(width^2 + 16 * height^2)/2 +
                    width^2 * log(
                        (4 * height + sqrt(width^2 + 16 * height^2))/width
                        )
                    /(8*height)
    putStrLn $ "Parabola length is: " ++ show arcLength

prompt x = do
    putStr x
    number <- getLine
    return number
