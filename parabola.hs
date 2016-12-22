-- Calculate Parabola results

main :: IO ()
main = do
    -- Grab the height
    height <- prompt "Please provide the height: "
    -- Grab the width
    width <- prompt "Please provide the width: "
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

-- Take a string from the user and convert into a Float.
prompt :: String -> IO Float
prompt x = do
    putStr x
    number <- getLine
    return (read number :: Float)
