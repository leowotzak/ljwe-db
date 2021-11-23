import Head from 'next/head'
import Link from 'next/link'

export default function Home() {
  return (
    <div className="container">
      test
      <Link href="/dash">
        <a>this page!</a>
      </Link>
    </div>
  )
}
