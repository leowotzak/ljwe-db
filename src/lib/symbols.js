
export async function getSymbols() {
    const res = await fetch("https://floating-headland-47828.herokuapp.com/ljwe/symbol")
    return res.json()
}
