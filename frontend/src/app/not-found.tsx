import Link from 'next/link'
import { Button } from '@/components/ui/Button'

export default function NotFound() {
  return (
    <div className="flex flex-col items-center justify-center min-h-[400px] p-4">
      <h2 className="text-2xl font-bold text-gray-900 mb-4">页面未找到</h2>
      <p className="text-gray-600 mb-6">抱歉，您访问的页面不存在</p>
      <Link href="/">
        <Button variant="default">
          返回首页
        </Button>
      </Link>
    </div>
  )
}
