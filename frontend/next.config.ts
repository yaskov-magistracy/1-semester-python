import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  async rewrites() {
    if (process.env.NODE_ENV === "production")
      return []; // Empty for production

    return [
      {
        source: '/api/:slug*',
        destination: 'http://localhost:8000/api/:slug*',
      },
    ]
  },
};

export default nextConfig;
