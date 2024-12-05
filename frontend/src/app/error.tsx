'use client'

import { useEffect } from 'react'
import { Button } from '@/components/ui/Button'

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string }
  reset: () => void
}) {
  useEffect(() => {
    console.error(error)
  }, [error])

  return (
    <div className="flex flex-col items-center justify-center min-h-[400px] p-4">
      <h2 className="text-2xl font-bold text-gray-900 mb-4">出错了</h2>
      <p className="text-gray-600 mb-6">抱歉，加载页面时出现了问题</p>
      <Button
        onClick={reset}
        variant="default"
      >
        重试
      </Button>
    </div>
  )
}
