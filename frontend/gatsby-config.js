/**
 * Configure your Gatsby site with this file.
 *
 * See: https://www.gatsbyjs.com/docs/gatsby-config/
 */

module.exports = {
  /* Your site config here */
  proxy: {
    prefix: "/ljwe",
    url: "http://localhost:8000"
  },

  plugins: [],
}

