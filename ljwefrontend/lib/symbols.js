
export async function getSymbols() {
    const res = await fetch("http://localhost:8000/ljwe/symbol")
    return res.json()
}
