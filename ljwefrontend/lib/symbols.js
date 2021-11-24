
export async function getSymbols() {
    const res = await fetch("https://blooming-journey-16393.herokuapp.com/ljwe/symbol")
    return res.json()
}
