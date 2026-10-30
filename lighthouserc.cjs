module.exports = {
  ci: {
    collect: {
      staticDistDir: './site',
      numberOfRuns: 3,
      url: [
        'http://localhost/',
        'http://localhost/docs/RESEARCH_NEWS/',
        'http://localhost/docs/COMPARISON_ENGINE/',
        'http://localhost/docs/INDUSTRY_TIMELINE/',
        'http://localhost/models/catalog/gls-0050/',
        'http://localhost/models/catalog/gls-0047/',
        'http://localhost/models/catalog/gls-0048/',
        'http://localhost/docs/faq/',
        'http://localhost/docs/faq/02-buying/',
        'http://localhost/guides/smart-glasses-without-cameras/',
      ],
      settings: {
        chromeFlags: '--headless --no-sandbox',
      },
    },
    assert: {
      assertions: {
        'categories:performance': ['warn', {minScore: 0.8}],
        'categories:accessibility': ['warn', {minScore: 0.9}],
        'categories:best-practices': ['warn', {minScore: 0.9}],
        'categories:seo': ['warn', {minScore: 0.9}],
        'largest-contentful-paint': ['warn', {maxNumericValue: 2500}],
        'cumulative-layout-shift': ['warn', {maxNumericValue: 0.1}],
        'total-blocking-time': ['warn', {maxNumericValue: 200}],
      },
    },
    upload: {
      target: 'filesystem',
      outputDir: './lhci-results',
    },
  },
};
