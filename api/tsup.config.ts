import { defineConfig } from 'tsup'

export default defineConfig({
    target: 'node18',
    format: 'esm',
    entry: ['src'],
    outDir: 'build',
    skipNodeModulesBundle: true
})
