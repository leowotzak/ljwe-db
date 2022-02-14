import React, { useState, useEffect } from "react";
import { PageLayout, BlogLink } from "../components";
import { Container, Row, Col } from "react-bootstrap";

// import { getSymbols } from "../lib/blog";

// export async function getStaticProps() {
//   const allBlogPosts = await getSymbols();

//   return {
//     props: { allBlogPosts },
//   };
// }

export default function Blog() {
  return (
    <PageLayout>
      <Container>
        <h1>This is the blog page</h1>
        <h3>This is a short subtitle describing what the content is</h3>
        <hr />
        {[1, 2, 3, 4].map((i) => (
          <BlogLink postNumber={i} />
        ))}
      </Container>
    </PageLayout>
  );
}
